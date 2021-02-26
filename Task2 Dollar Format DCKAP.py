from num2words import num2words 
s = "1234567"
currency = "${}".format(int(s))
if '$' in currency:
    print(num2words(currency[1:])+ ' dollar%s' % ('s' if int(s[1:]) != 1 else ''))

    