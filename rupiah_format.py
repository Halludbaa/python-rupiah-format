def rupiah_format(amount: int) -> str:
    return "Rp. {:,.2f}".format(amount).replace(",", ".")[::-1].replace(".", ",", 1)[::-1]


print(rupiah_format(10_000_000)) #output: Rp. 10.000.000,00