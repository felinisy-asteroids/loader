from loader.loader import Loader
from utils.logger import logger
from utils.settings import settings


def main(request):
    request_json = request.get_json()
    bucket_name = request_json.get("bucket")

    if not bucket_name:
        return {"error": "bucket name not provided"}, 400

    try:
        loader = Loader()
        loader.load(bucket_name)
        return {"status": "success"}, 200
    except Exception as e:
        logger.error(f"Load failed: {e}")
        return {"error": str(e)}, 500

#
# if __name__ == "__main__":
#     class MockRequest:
#         def get_json(self):
#             return {"bucket": "asteroids-etl"}
#
#     response, status = main(MockRequest())
#     print(f"Status: {status}")
#     print(f"Response: {response}")