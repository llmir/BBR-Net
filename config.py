CONFIG = {
    'TRAIN_PATH': '/data1/huangyj/ophthamology/dataset/lesion/HE/cropped_resize_output/cropped_img_train/gt.csv',
    'TEST_PATH': '/data1/huangyj/ophthamology/dataset/lesion/HE/cropped_resize_output/cropped_img_test/gt.csv',
    # 'TRAIN_PATH': '/data1/huangyj/ophthamology/dataset/lesion/cropped_img_train/gt.csv',
    # 'TEST_PATH': '/data1/huangyj/ophthamology/dataset/lesion/cropped_img_test/gt.csv',
    'SAVE_PATH': '../result/rectify_net/bbr_net_lite_giou.pt',
    'RECORD_PATH': '../result/rectify_net/bbr_net_lite_giou.rec',
    'PRETRAINED_PATH': None,
    'LEARNING_RATE': 0.003,
    'INPUT_SIZE': 128,
    'BOTTLENECK_SIZE': 512,
    'NUM_CLASS': 4,
    'BATCH_SIZE': 64,
    'EPOCHS': 100,
    'DATA_AUGMENTATION': {
        'scale': (1 / 1.15, 1.15),
        'stretch_ratio': (0.7561, 1.3225),  # (1/(1.15*1.15) and 1.15*1.15)
        'ratation': (-30, 30),
        'translation_ratio': (20 / 128, 20 / 128),  # 20 pixel in the report
        'sigma': 0.5
    }
}