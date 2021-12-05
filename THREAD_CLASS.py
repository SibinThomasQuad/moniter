import threading

class DomainOperations:

    def __init__(self):
        self.domain_ip = ''
        self.website_thumbnail = ''

    def resolve_domain(self):
        self.domain_ip = 'foo'

    def generate_website_thumbnail(self):
        self.website_thumbnail= 'bar'

    def run(self):
        t1 = threading.Thread(target=self.resolve_domain)
        t2 = threading.Thread(target=self.generate_website_thumbnail)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(self.domain_ip, self.website_thumbnail)

if __name__ == '__main__':
    d = DomainOperations()
    d.run()
