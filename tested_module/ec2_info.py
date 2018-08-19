""" EC2 mock information functions """

img_matrix = {
    1: "tiny",
    2: "small",
    4: "medium",
    16: "large",
    9: "xlarge"
}

PRICE_MATRIX = {
    "default": {
        "tiny": 0.41, "small": 0.45, "medium": 0.63, "large": 0.99, "xlarge": 1.20
    },
    "eu": {
        "tiny": 0.40, "medium": 0.61
    },
    "ap": {
        "xlarge": 1.51
    }
}


def calc_image(cpu, mem):
    """
        This function mocks calculation of required image size provided
        a required memory and number of CPUs
    """
    return img_matrix[cpu * mem]


def get_image_price(image_size, region):
    """
        This function mocks calculation of image price per hour provided the image size
        and the deployment region
    """
    if (region in PRICE_MATRIX and image_size in PRICE_MATRIX[region]):
        return PRICE_MATRIX[region][image_size]

    return PRICE_MATRIX["default"][image_size]
