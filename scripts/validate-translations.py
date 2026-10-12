
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
MARKER = "[NEEDS TRANSLATION]"
def load(path):
    with path.open(encoding="utf-8") as f: return json.load(f)
def placeholders(value):
    return sorted(re.findall(r"\{[A-Za-z_][A-Za-z0-9_]*\}", value))
def main():
    errors=[]
    try: index=load(ROOT/"languages-index.json")
    except Exception as e:
        print("ERRO no índice:", e); return 1
    packs={}
    for item in index.get("languages", []):
        code, filename=item.get("code"), item.get("file")
        if not isinstance(code,str) or not isinstance(filename,str):
            errors.append(f"Entrada inválida no índice: {item!r}"); continue
        path=(ROOT/filename).resolve()
        if ROOT.resolve() not in path.parents:
            errors.append(f"{code}: caminho fora do repositório"); continue
        if not path.is_file():
            errors.append(f"{code}: arquivo não encontrado: {filename}"); continue
        try: data=load(path)
        except Exception as e:
            errors.append(f"{filename}: JSON inválido: {e}"); continue
        if data.get("language") != code: errors.append(f"{filename}: código de idioma divergente")
        if not isinstance(data.get("strings"),dict):
            errors.append(f"{filename}: 'strings' precisa ser objeto"); continue
        packs[code]=data["strings"]
    base=packs.get("pt-BR")
    if base is None: errors.append("Idioma base pt-BR ausente")
    else:
        for code, strings in packs.items():
            for key in sorted(set(base)-set(strings)): errors.append(f"{code}: chave ausente: {key}")
            for key in sorted(set(strings)-set(base)): errors.append(f"{code}: chave extra: {key}")
            for key in sorted(set(base)&set(strings)):
                val=strings[key]
                if not isinstance(val,str) or not val.strip(): errors.append(f"{code}: valor vazio/não textual: {key}"); continue
                if MARKER in val: errors.append(f"{code}: tradução pendente: {key}")
                if isinstance(base[key],str) and placeholders(val)!=placeholders(base[key]):
                    errors.append(f"{code}: placeholders divergentes: {key}")
    if errors:
        print(f"FALHA: {len(errors)} problema(s)")
        print("\n".join("- "+e for e in errors))
        return 1
    print(f"OK: {len(packs)} idiomas; chaves e placeholders consistentes.")
    return 0
if __name__=="__main__": sys.exit(main())
