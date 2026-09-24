# processo-cnj

Programa em Python que recebe números de processo no padrão CNJ (`NNNNNNN-DD.AAAA.J.TR.OOOO`), com ou sem pontuação. O script rejeita entradas inválidas, separa os componentes, identifica o segmento da Justiça e o tribunal, monta o alias do endpoint do DataJud e valida os dígitos verificadores.

## Como rodar

```bash
python processo.py

```

## Testes

Para executar os testes automatizados com o `pytest`:

```bash
pytest test_processo.py -v

```

Resultado esperado:

```text
============================== test session starts ===============================
platform win32 -- Python 3.13.9, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\lubca\projetos\processo-cnj
collected 4 items

test_processo.py::test_check_digit PASSED                                 [ 25%]
test_processo.py::test_punctuation PASSED                                 [ 50%]
test_processo.py::test_invalid_inputs PASSED                              [ 75%]
test_processo.py::test_builds_trf_and_trt_aliases PASSED                                       [100%]

============================== 4 passed in 0.07s ===============================

```

## Exemplo de Execução

```text
Número do processo: 0000832-35.2018.4.01.3202
{'sequential_number': '0000832', 'check_digit': '35', 'year': '2018', 'judiciary_branch': '4', 'court_code': '01', 'origin_unit': '3202'}
Justiça Federal
api_publica_trf1
True
```
