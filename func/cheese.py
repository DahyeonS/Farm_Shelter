from django.core.files.storage import FileSystemStorage
import pathlib, json, os
from tensorflow import keras

UPLOAD_FOLDER = os.getcwd() + '/media/ml/classification'

def cheese_test(new_name) :
    model = keras.models.load_model('cheese.h5')

    img_height = img_width = 256
    batch_size = 32
    class_names = ['bloomy', 'blue', 'fresh', 'hard', 'semi-soft', 'washed-rind']

    test_img = keras.utils.image_dataset_from_directory(
        pathlib.Path("media/ml"),
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    result = model.predict(test_img) # 2차원 배열의 정수 6개 예시 - [[-5.5395255 -2.0526016 -2.0175126  5.378921   5.791862   3.880874 ]]

    new_result = []
    size = result.max() - result.min()
    for r in result[0] :
        if r > 0 :
            new_result.append(round((r / size) * 100))
        else :
            if r - result.min() > 0 :
                new_result.append(round((r - result.min()) / size * 100))
            else :
                new_result.append(round((r - result.min()) / -size * 100))

    sort_result = sorted(new_result, reverse=True)[:4]
    data = {}
    for num in sort_result :
        index = new_result.index(num)
        data[class_names[index]] = new_result[index]

    os.remove(UPLOAD_FOLDER + '/' + new_name)

    return json.dumps(data)

def image_upload(file) :
    if file :
        new_name = ('test.' + str(file.name).split('.')[-1])
        fs = FileSystemStorage(location=UPLOAD_FOLDER, base_url=UPLOAD_FOLDER)
        fs.save(new_name, file)
        return new_name