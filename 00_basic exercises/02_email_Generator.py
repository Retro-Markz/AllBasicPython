
print()
full_name = "  Marco Cubedo "
print(f'User Name: {full_name}')
userName = full_name.replace(" ", '').lower().strip()
# userName = userName.lower()
# userName = userName.replace(" ", '')

companyName = "  Amazing Devs"
print(f'Company Name: {companyName}')
userDomain = companyName.replace(" ", '').lower().strip()
# userDomain = userDomain.strip()
# userDomain = userDomain.replace(" ", '')

extension = " . com.Mx"
extension = extension.replace(' ','').lower().strip()
# extension = extension.strip()
# extension = extension.replace(' ','')


print()
email = userName + "@" + userDomain + extension

print(email)
print()


