from api_helper import Config
from http_client import HttpClient
import pytest
import os


@pytest.fixture(scope="class")
def resource_setup(request):
    request.cls.resource = "resource"
    yield
    # Teardown code
    del request.cls.resource

@pytest.fixture(scope="class")
def setup_data(request):
    print("Setting up class")
    request.cls.setup_data = "setup_data"
    yield
    del request.cls.setup_data

@pytest.mark.usefixtures("resource_setup", "setup_data")
class TestApi:
    package_quantity = 6
    package_id = "merhaba-7days-1gb"
    esim_type = "Prepaid"

    @classmethod
    def setup_class(cls):
        # Class-level setup, runs once before all tests
        config = Config()
        cls.class_resource = "class_resource"
        cls.http_client_obj = HttpClient(base_url=config.base_url(), client_id=os.environ.get('CLIENT_ID') ,
                                         client_secret=os.environ.get('CLIENT_SECRET') )

    @classmethod
    def teardown_class(cls):
        # Class-level teardown, runs once after all tests
        print("\nClass-level teardown")
        del cls.class_resource

    def test_post_esims(self):
        response = TestApi.http_client_obj.post('/v2/orders', {"quantity": "{}".format(TestApi.package_quantity),
                                                               "package_id": "{}".format(TestApi.package_id)})
        #print(response["data"])
        print("verify POST eSims")
        assert response["data"]["package_id"] == TestApi.package_id, "eSIM POST response: package slug did not match"
        assert response["data"]["quantity"] == TestApi.package_quantity, "eSIM POST response: package quantity did not match"
        assert response["meta"]["message"] == "success"
        print("POST endpoint: post an eSIM order verified")


    def test_get_esims(self):
        print("Verify GET eSims")
        response = TestApi.http_client_obj.get('/v2/sims', {"include": "order,order.status,order.user",
                                                            "limit": "{}".format(TestApi.package_quantity)})
        assert len(response["data"]) == TestApi.package_quantity, "eSIM get response: package quantity did not match"
        for i in range(len(response["data"])):
            #print("package_id:{}".format(response["data"][i]["simable"]["package_id"]))
            #print("esim_type:{}".format(response["data"][i]["simable"]["esim_type"]))
            assert response["data"][i]["simable"]["package_id"] == TestApi.package_id, "eSIM GET response: package slug did not match"
            assert response["data"][i]["simable"]["esim_type"] == TestApi.esim_type, "eSIM GET response: eSim type did not match"
        print("GET endpoint: eSIM package quantity and package slug verified")