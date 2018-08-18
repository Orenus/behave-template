import random

# returns a fake instance with randomized fqdn


def start_app(size, region, image):
    return {
        "size": size,
        "region": region,
        "image": image,
        "fqdn": str(random.randint(0, 1000000)) + "random.someFakeDomain.com",
        "status": "started"
    }

# returns True/False randomly


def test_port(fqdn, port):
    return (random.randint(0, 5) == 1)
