import face_recognition as fr
import urllib



def compare_faces(file1, file2):
    # Load the jpg files into numpy arrays
    image1 = fr.load_image_file(file1)
    image2 = fr.load_image_file(file2)

    # Get the face encodings for 1st face in each image file
    image1_encoding = fr.face_encodings(image1)[0]
    image2_encoding = fr.face_encodings(image2)[0]

    # Compare faces and return True / False
    results = fr.compare_faces([image1_encoding], image2_encoding)
    return results[0]


# Each face is tuple of (Name,people)
known_faces = [('ronaldo', 'people/ronaldo.jpg'),
               ('trump', 'people/trump.jpg'),
                ('brad', 'people/brad.jpg'),
                ('mane', 'people/putin.jpg'),
                ('obama', 'people/obama.jpg')

               ]

def face_rec(file):

    """
    Return name for a known face, otherwise return 'Uknown'.
    """
    for name, known_face in known_faces:
        if compare_faces(known_face, file ):
            return name
    return 'Unknown'



