def significant_difference_threshold(image_obj):
    # 5% of the screenshot should be different to be considered a significant difference
    DIFFERENCE_THRESHOLD = 0.00004

    # Load the image
    image = image_obj.load()

    different_pixels_counter = 0
    image_pixel_count = image_obj.size[0] * image_obj.size[1]

    for x, y in zip(range(image_obj.size[0]), range(image_obj.size[1])):
        if float(image[x, y]) != 0:
            different_pixels_counter += 1

    difference = float(different_pixels_counter / image_pixel_count)

    return DIFFERENCE_THRESHOLD >= difference
