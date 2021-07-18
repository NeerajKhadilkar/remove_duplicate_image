
from PIL import Image  
import PIL  
import imagehash
import os


reference_fold = r"C:\Users\Neeraj\Desktop\test"

def remove_images_from_dir():

    dico={}

    # add as many directories here in list you want
    reference_directory=[reference_fold]

    for ref_path in reference_directory:

        for imageName in os.listdir(ref_path):

            print(imageName)

            fullImage=os.path.join(ref_path,imageName)
            
            image = Image.open(fullImage)
            
            phash = str(imagehash.phash(image))
            print(phash)

            if fullImage not in dico.keys():
                dico[fullImage]=phash
            
            print()


    print()

    result = {}

    for key, value in dico.items():

        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)


    print("final_dictionary", result)

    for key,val in result.items():
        if len(val)>1:
            print(val)

            #print()

            # removing redundant images except for one
            
            for removed_file in val[1:]:
                if os.path.exists(removed_file):
                    os.remove(removed_file)
                    print(removed_file," file removed..")
                else:
                    print(f"The {removed_file} file does not exist")


            print()


remove_images_from_dir()








