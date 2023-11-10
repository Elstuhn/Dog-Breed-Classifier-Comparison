# Dog-Breed-Classifier-Comparison
Model comparison between resnet, vgg and alexnet to classify different breeds of dogs 

# Brief
This program runs vgg, resnet and alexnet on images of dogs with different breeds and compares the models according to three metrics, classification power on breed, classification power on detecting if it's a dog and classification power on detecting if it's not a dog.

# Usage
### For running debug mode where you can see all outputs
1. run check_images.py

### For running pre-loaded dog images
1. run `sh run_models_batch.sh`
2. Overall results for all three models will be updated in the (model)_pet-images.txt files accordingly

### For running uploaded images
1. Upload whatever image you want into the `uploaded_images` folder (doesn't need to be a dog)
2. run `sh run_models_batch_uploaded.sh`
3. Results for all three models will be updated in the (model)_uploaded-images.txt files accordingly


<br>
<sub><sup>This was done for the AWS AI & ML Scholarship 2023 Winter Cohort program held on Udacity.</sup></sub>
