import matplotlib.pyplot as plt
import numpy as np

def get_var_name(variable):
    """Print the name of variable

    Args:
        variable (_type_): _description_

    Returns:
        _type_: String
        
    Examples:
        apple = 3
        print(get_var_name(apple))
        -> "apple"
    """
    globals_dict = globals()
    name = [var_name for var_name in globals_dict if globals_dict[var_name] is variable]
    print(name)

def show_images(list_of_images:list, rows:int, columns:int, size_x:int=10, size_y:int=10):
    """
    Show all the images in the list
    Example:
        img_to_show = [img_bouding_rect, img_approx_poly]
        show_images(img_to_show,1,2,10,10)
    """
    if len(list_of_images)>(rows*columns):
        return "Check the input"
    plt.figure(figsize=(size_x, size_y))
    for i in range(len(list_of_images)):
        plt.subplot(rows, columns, i+1);plt.imshow(list_of_images[i]);plt.title(get_var_name(list_of_images[i]));