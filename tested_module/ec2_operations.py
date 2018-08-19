""" EC2 mock operations functions """
import random


def start_app(size, region, image):
    """
        This function supposedly starts an EC2 instance provided deployment size, deployment region,
        and image. It returns an instance object with a randomly generated fqdn and status
     """
    return {
        "size": size,
        "region": region,
        "image": image,
        "fqdn": str(random.randint(0, 1000000)) + "random.someFakeDomain.com",
        "status": "started"
    }

# returns True/False randomly


def test_port(fqdn, port):
    """
        This function supposedly checks accessibility of instance provided its fqdn and the
        port. It returns a random True / False (just to simulate success failure)
    """
    return random.randint(0, 5) == 1
