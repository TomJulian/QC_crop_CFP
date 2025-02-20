import M0_Preprocess.EyeQ_process_main as M0_EQ
import M1_Retinal_Image_quality_EyePACS.test_outside as M1_EP
import M1_Retinal_Image_quality_EyePACS.merge_quality_assessment as M1_QA

logging.basicConfig(
    level=logging.INFO,
    filename="data.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


if __name__ == "__main__":

    #add argument parser to specify direct values to config

    parser = argparse.ArgumentParser(description="A simple command-line tool.")
    parser.add_argument("-i", "--image_dir", help="path to image directory", type=str)
    parser.add_argument("-r", "--results_dir", type=str, help="path to results directory")
    args = parser.parse_args()

    if args.image_dir:
        config.image_dir = args.image_dir
    if args.results_dir:
        config.results_dir = args.results_dir
    
    print("\n--------------------\nRunning PreProcessing")
    # preprocessing
    M0_EQ.EyeQ_process(config)

    # Eye Quality deep learning assesment
    print("\n--------------------\nRunning Image Quality Assesment")
    M1_EP.M1_image_quality(config)
    M1_QA.quality_assessment(config)

    
