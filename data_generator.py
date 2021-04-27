import names

full_name_list = []

for a in range(0, 1001):
    full_name_list.append(names.get_full_name())

print(full_name_list)

#import random
#domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
#letters = string.ascii_lowercase[:12]

#def get_random_domain(domains):
    #return random.choice(domains)

#def get_random_name(letters, length):
    #return ''.join(random.choice(letters) for i in range(length))

#def generate_random_emails(nb, length):
    #return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]

#def main():
    #print(generate_random_emails(10, 7))

#if __name__ == "__main__":
    #main()
 
#import string

#for i in range(3):
    #result_str = ''.join(random.sample(string.ascii_lowercase, 8))
    #print(result_str)