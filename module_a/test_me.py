img_matrix = {
    1: "tiny",
    2: "small",
    4: "medium",
    16: "large",
    9: "xlarge"
}

price_matrix = {
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
    return img_matrix[cpu * mem]


def get_image_price(image, region):
    if (region in price_matrix and image in price_matrix[region]):
        return price_matrix[region][image]

    return price_matrix["default"][image]
