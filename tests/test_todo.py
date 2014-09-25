import unittest


class TestTodoCheck(unittest.TestCase):

    root = 'http://private-35a51-restfest2014.apiary-mock.com/'

    def test_todo_check_scenario(self):

        client = Hyperclient(root=self.root)

        rootObject = client.resolve()

        user = client.follow('userCreate', data={
            
        })
        

        # from urllib2 import Request, urlopen

        # request = Request('http://private-35a51-restfest2014.apiary-mock.com/')

        # response_body = urlopen(request).read()
        # print response_body
