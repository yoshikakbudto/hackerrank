# Problem: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
# Score: 20
def fun(s):
    # return True if s is a valid email, else return False

    # Only one dog allowed
    if not len(s.split('@')) == 2:
        return False
    else:
        username, website = s.split('@')

    # Only one dot allowed wich splits website name and extension
    if not len(website.split('.')) == 2:
        return False
    else:
        wsname, wsext = website.split('.')

    if  username.replace('_','').replace('-','').isalnum() \
        and wsext.isalpha() and 0 < len(wsext) < 4 \
        and wsname.isalnum():
        return True

    return False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)