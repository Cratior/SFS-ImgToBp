# SFS-ImgToBp (Pre-Release)

**NOTE: This version of SFS-ImgToBp is currently in pre-release and is not optimized for performance. Expect longer processing times and blueprints with a large number of parts.**

SFS-ImgToBp is a Python script that takes a PNG or JPG image as input and generates a blueprint for the game SpaceFlight Simulator.

## How to Use

1. Download and run the `start.bat` file.
2. Choose an example image or provide your own image.
3. Wait for the script to process the image.
4. The generated blueprint file will automatically download to the same folder as the script.
5. Move the downloaded folder to your SpaceFlight Simulator directory, specifically to `saving/blueprint`.

⚠️ **Important** ⚠️
- The input image should have a **white background**. It is recommended that the image is an outline of what you want to create.
- Any colors can be used in the image except for white, as the script converts those colors to parts.
- Currently, the script only uses one size fuel tank. I have attempted to fix this, but it's not working properly. I will add support for different fuel tank sizes in a future update.
- If the input image is large, consider lowering its resolution or using the scale factor. The scale factor only reduces the size of the craft and doesn't affect the number of parts generated. I will try to update it so that it won't output thousands of fuel tanks.

## Using the Generated Blueprint as a Template

The blueprint generated by SFS-ImgToBp can serve as a starting point or template for building your spacecraft in SpaceFlight Simulator. Once you have the blueprint file, you can import it into the game and make further modifications to refine your design.

The current pre-release version of SFS-ImgToBp may generate blueprints with a large number of parts, which can impact the performance of the game. Please be aware that these blueprints might require additional optimization or adjustments to ensure smooth gameplay.

Feel free to contribute to the project, report any issues, or suggest improvements to enhance the functionality of SFS-ImgToBp!

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please reach out to me on Discord at `cratior#7703`.

## License

This project is licensed under the [MIT License](LICENSE).

## Example
![CD2D0EE1-DED4-4BCB-988E-2EB6814A6CE2](https://github.com/Cratior/SFS-ImgToBp/assets/55932656/601fa77a-4f1a-4e65-8058-5444c260d0d1)
![87A8B191-5F1D-4748-9F2D-96C06D70E981](https://github.com/Cratior/SFS-ImgToBp/assets/55932656/60cf70b7-8cfa-4115-ac19-bc1c08722df9)

## Ac-130
![937166B7-6D39-4DBB-AB77-7EF8D9FFC87F](https://github.com/Cratior/SFS-ImgToBp/assets/55932656/003d7f73-319b-4608-bdbd-52173d8ba0a3)
![854E5D81-7AC0-4410-9F21-A23607F53377](https://github.com/Cratior/SFS-ImgToBp/assets/55932656/cc9f2185-9972-4689-b022-ca10cd4106ef)

## A-10
![4E82DFDF-6476-4408-A735-C1AEEBCB24F8](https://github.com/Cratior/SFS-ImgToBp/assets/55932656/dcbae46c-aa31-4dbf-ade0-a541ac18b925)
![45565A8E-E505-45BE-AC6B-1CC73EE4975B](https://github.com/Cratior/SFS-ImgToBp/assets/55932656/9a3241f2-897e-4fb9-90d1-c0729709ca07)

## iss
![edu_what_is_iss_58](https://github.com/Cratior/SFS-ImgToBp/assets/55932656/6f2bd604-1894-4347-8035-59c484ce88bb)
![sat](https://github.com/Cratior/SFS-ImgToBp/assets/55932656/ffae9951-d659-4ea2-95d6-a37392e22c36)
