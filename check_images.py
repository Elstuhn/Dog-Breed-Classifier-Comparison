#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
# PROGRAMMER: Elston Tan
# DATE CREATED: 3/11/2023                           
# REVISED DATE: 9/11/2023
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    start_time = time()
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)
    
    classify_images(in_arg.dir, results, in_arg.arch)
   
    check_classifying_images(results)    
    # TODO 4: Define adjust_results4_isadog function within the file adjust_results4_isadog.py
    # Once the adjust_results4_isadog function has been defined replace 'None' 
    # in the function call with in_arg.dogfile  Once you have done the 
    # replacements your function call should look like this: 
    #          adjust_results4_isadog(results, in_arg.dogfile)
    # Adjusts the results dictionary to determine if classifier correctly 
    # classified images as 'a dog' or 'not a dog'. This demonstrates if 
    # model can correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)


    # TODO 5: Define calculates_results_stats function within the file calculates_results_stats.py
    # This function creates the results statistics dictionary that contains a
    # summary of the results statistics (this includes counts & percentages). This
    # dictionary is returned from the function call as the variable results_stats    
    # Calculates results of run and puts statistics in the Results Statistics
    # Dictionary - called results_stats
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)

    print_results(results, results_stats, in_arg.arch, True, True)
    
    end_time = time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

if __name__ == "__main__":
    main()
