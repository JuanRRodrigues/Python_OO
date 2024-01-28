def create_account(number, titular, saldo, limite):
    account = {"number": number, "titular": titular, "saldo": saldo, "limite": limite}
    return account


def deposita(account, valor):
    account["saldo"] += valor


def saca(account, valor):
    account["saldo"] -= valor


def extrato(account):
    print("Saldo é {}".format(account["saldo"]))
