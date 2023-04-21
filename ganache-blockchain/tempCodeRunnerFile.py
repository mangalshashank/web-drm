 # # Convert text to binary representation
    # binary_text = text_to_binary(text)

    # # Get the shape of the image
    # height, width, channels = image.shape

    # # Flatten the image into a 1D array
    # image_data = image.ravel()

    # # Perform the Fourier transform
    # image_fft = spfft.fft(image_data)

    # # Embed the text into the frequency domain
    # text_length = len(binary_text)
    # for i in range(text_length):
    #     if binary_text[i] == '1':
    #         image_fft[i] = image_fft[i] + 10

    # # Perform the inverse Fourier transform
    # image_ifft = spfft.ifft(image_fft)

    # # Reshape the image to its original shape
    # image_embedded = np.real(image_ifft).reshape(height, width, channels)

    # # Save the embedded image
    # cv2.imwrite("embedded_image.png", image_embedded)

    # print("Text embedded successfully!")