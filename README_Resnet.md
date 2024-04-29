Since we're only ResNet as a baseline, I utilized some publicly available code:
For ResNet, I used the PyTorch implementation: https://github.com/pytorch/vision/blob/main/torchvision/models/resnet.py 

I played around with both architectures a lot to see if I could get them to work better for our dataset. 
When I first tried ResNet, I found that it was overfitting pretty badly, with training accuracy getting above 90% while validation and test accuracies remained around 50-60%. I then considered some strategies to combat overfitting, such as adding dropout. I found that there were some papers discussing where to add dropout in ResNet, but that the status quo seemed to be to do it after average pooling. 
Adding dropout didn't help much, and I also tried a different pooling method (AvgPool2d instead of AdaptiveAvgPool2d) just to see if it made a difference, but overfitting was still a problem.
Now, I realize that the issue was likely that I had forgotten to resize the images. The images in the dataset are 48x48, but ResNet requires images to be 224x224. 

Upon re-running ResNet-34 for 20 epochs, the maximum training accuracy obtained was 67.94% and the test accuracy was 56.92%, which is not great but the discrepancy is much smaller. The training accuracy was still increasing at the 20th epoch, but since ResNet takes so long to run, I had limited it to that number of epochs.

resnetfix.pth can be accessed here: https://drive.google.com/file/d/1E3WmcKy8pleLBaQDkpxeqxDtehL1snXf/view?usp=sharing