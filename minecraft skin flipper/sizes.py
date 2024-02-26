import numpy as np


def size(img: np.ndarray, type='steve') -> dict:
    if not isinstance(img, np.ndarray):
            try:
                    img = np.ndarray(img)
            except:
                    return None
    if type == 'alex':
        alex = {'head_top': img[0:8, 8:16],
                'head_bottom': img[0:8, 16:24],
                'head_right': img[8:16, 0:8],
                'head_front': img[8:16, 8:16],
                'head_left': img[8:16, 16:24],
                'head_back': img[8:16, 24:32],

                'hat_top': img[0:8, 40:48],
                'hat_bottom': img[0:8, 48:56],
                'hat_right': img[8:16, 32:40],
                'hat_front': img[8:16, 40:48],
                'hat_left': img[8:16, 48:56],
                'hat_back': img[8:16, 56:64],

                'body_top': img[16:20, 20:28],
                'body_bottom': img[16:20, 28:36],
                'body_right': img[20:32, 16:20],
                'body_front': img[20:32, 20:28],
                'body_left': img[20:32, 28:32],
                'body_back': img[20:32, 32:40],

                'jacket_top': img[32:36, 20:28],
                'jacket_bottom': img[32:36, 28:36],
                'jacket_right': img[36:48, 16:20],
                'jacket_front': img[36:48, 20:28],
                'jacket_left': img[36:48, 28:32],
                'jacket_back': img[36:48, 32:40],

                'rightLeg_top': img[16:20, 4:8],
                'rightLeg_bottom': img[16:20, 8:12],
                'rightLeg_right': img[20:32, 0:4],
                'rightLeg_front': img[20:32, 4:8],
                'rightLeg_left': img[20:32, 8:12],
                'rightLeg_back': img[20:32, 12:16],

                'rightPants_top': img[32:36, 4:8],
                'rightPants_bottom': img[32:36, 8:12],
                'rightPants_right': img[36:48, 0:4],
                'rightPants_front': img[36:48, 4:8],
                'rightPants_left': img[36:48, 8:12],
                'rightPants_back': img[36:48, 12:16],

                'leftLeg_top': img[48:52, 20:24],
                'leftLeg_bottom': img[48:52, 24:28],
                'leftLeg_right': img[52:64, 16:20],
                'leftLeg_front': img[52:64, 20:24],
                'leftLeg_left': img[52:64, 24:28],
                'leftLeg_back': img[52:64, 28:32],

                'leftPants_top': img[48:52, 4:8],
                'leftPants_bottom': img[48:52, 8:12],
                'leftPants_right': img[52:64, 0:4],
                'leftPants_front': img[52:64, 4:8],
                'leftPants_left': img[52:64, 8:12],
                'leftPants_back': img[52:64, 12:16],

                'rightArm_top': img[16:20, 44:47],
                'rightArm_bottom': img[16:20, 47:50],
                'rightArm_right': img[20:32, 40:44],
                'rightArm_front': img[20:32, 44:47],
                'rightArm_left': img[20:32, 47:51],
                'rightArm_back': img[20:32, 51:54],

                'rightSleeve_top': img[16:20, 44:47],
                'rightSleeve_bottom': img[16:20, 47:50],
                'rightSleeve_right': img[20:32, 40:44],
                'rightSleeve_front': img[20:32, 44:47],
                'rightSleeve_left': img[20:32, 47:51],
                'rightSleeve_back': img[20:32, 51:54],

                'leftArm_top': img[48:52, 36:49],
                'leftArm_bottom': img[48:52, 49:42],
                'leftArm_right': img[52:64, 32:36],
                'leftArm_front': img[52:64, 36:39],
                'leftArm_left': img[52:64, 39:43],
                'leftArm_back': img[52:64, 43:46],

                'leftSleeve_top': img[48:52, 52:55],
                'leftSleeve_bottom': img[48:52, 55:58],
                'leftSleeve_right': img[52:64, 48:52],
                'leftSleeve_front': img[52:64, 52:55],
                'leftSleeve_left': img[52:64, 55:59],
                'leftSleeve_back': img[52:64, 59:62]
                }
        return alex

    elif type == 'steve':
        steve = {'head_top': img[0:8, 8:16],
                 'head_bottom': img[0:8, 16:24],
                 'head_right': img[8:16, 0:8],
                 'head_front': img[8:16, 8:16],
                 'head_left': img[8:16, 16:24],
                 'head_back': img[8:16, 24:32],

                 'hat_top': img[0:8, 40:48],
                 'hat_bottom': img[0:8, 48:56],
                 'hat_right': img[8:16, 32:40],
                 'hat_front': img[8:16, 40:48],
                 'hat_left': img[8:16, 48:56],
                 'hat_back': img[8:16, 56:64],

                 'body_top': img[16:20, 20:28],
                 'body_bottom': img[16:20, 28:36],
                 'body_right': img[20:32, 16:20],
                 'body_front': img[20:32, 20:28],
                 'body_left': img[20:32, 28:32],
                 'body_back': img[20:32, 32:40],

                 'jacket_top': img[32:36, 20:28],
                 'jacket_bottom': img[32:36, 28:36],
                 'jacket_right': img[36:48, 16:20],
                 'jacket_front': img[36:48, 20:28],
                 'jacket_left': img[36:48, 28:32],
                 'jacket_back': img[36:48, 32:40],

                 'rightLeg_top': img[16:20, 4:8],
                 'rightLeg_bottom': img[16:20, 8:12],
                 'rightLeg_right': img[20:32, 0:4],
                 'rightLeg_front': img[20:32, 4:8],
                 'rightLeg_left': img[20:32, 8:12],
                 'rightLeg_back': img[20:32, 12:16],

                 'rightPants_top': img[32:36, 4:8],
                 'rightPants_bottom': img[32:36, 8:12],
                 'rightPants_right': img[36:48, 0:4],
                 'rightPants_front': img[36:48, 4:8],
                 'rightPants_left': img[36:48, 8:12],
                 'rightPants_back': img[36:48, 12:16],

                 'leftLeg_top': img[48:52, 20:24],  ######         NOT CORRECTED
                 'leftLeg_bottom': img[48:52, 24:28],
                 'leftLeg_right': img[52:64, 16:20],
                 'leftLeg_front': img[52:64, 20:24],
                 'leftLeg_left': img[52:64, 24:28],
                 'leftLeg_back': img[52:64, 28:32],

                 'leftPants_top': img[48:52, 4:8],
                 'leftPants_bottom': img[48:52, 8:12],
                 'leftPants_right': img[52:64, 0:4],
                 'leftPants_front': img[52:64, 4:8],
                 'leftPants_left': img[52:64, 8:12],
                 'leftPants_back': img[52:64, 12:16],

                 'rightArm_top': img[16:20, 44:47],
                 'rightArm_bottom': img[16:20, 47:50],
                 'rightArm_right': img[20:32, 40:44],
                 'rightArm_front': img[20:32, 44:47],
                 'rightArm_left': img[20:32, 47:51],
                 'rightArm_back': img[20:32, 51:54],

                 'rightSleeve_top': img[16:20, 44:47],
                 'rightSleeve_bottom': img[16:20, 47:50],
                 'rightSleeve_right': img[20:32, 40:44],
                 'rightSleeve_front': img[20:32, 44:47],
                 'rightSleeve_left': img[20:32, 47:51],
                 'rightSleeve_back': img[20:32, 51:54],

                 'leftArm_top': img[48:52, 36:49],
                 'leftArm_bottom': img[48:52, 49:42],
                 'leftArm_right': img[52:64, 32:36],
                 'leftArm_front': img[52:64, 36:39],
                 'leftArm_left': img[52:64, 39:43],
                 'leftArm_back': img[52:64, 43:46],

                 'leftSleeve_top': img[48:52, 52:55],
                 'leftSleeve_bottom': img[48:52, 55:58],
                 'leftSleeve_right': img[52:64, 48:52],
                 'leftSleeve_front': img[52:64, 52:55],
                 'leftSleeve_left': img[52:64, 55:59],
                 'leftSleeve_back': img[52:64, 59:62]
                 }
        return steve
    else:
        return None
