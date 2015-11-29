import cv2
#Code snippet from OpenCV Example (Video.py)

def create_capture(webCam):
    code, image = webCam.read()
    print("Success code: " + str(code))
    cv2.imwrite("frame.jpg", image)

    #Can't Connect to WebCam
    if webCam is None or not webCam.isOpened():
        print 'Warning: unable to open video source: (Need Fallback function)'

#This may be used when run on the UDOO, we have to see how the OS assigns the source
'''def create_capture(source = 0):

    #Parse The source camera
    source = str(source).strip()
    chunks = source.split(':')

    # handle drive letter ('c:', ...)
    if len(chunks) > 1 and len(chunks[0]) == 1 and chunks[0].isalpha():
        chunks[1] = chunks[0] + ':' + chunks[1]
        del chunks[0]

    source = chunks[0]
    try: source = int(source)
    except ValueError: pass
    params = dict( s.split('=') for s in chunks[1:] )

    cap = None
    if source == 'synth':
        Class = classes.get(params.get('class', None), VideoSynthBase)
        try: cap = Class(**params)
        except: pass
    else:
        cap = cv2.VideoCapture(source)
        print(source)
        if 'size' in params:
            w, h = map(int, params['size'].split('x'))
            print(str(w) + str(h))
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

        code, image = cap.read()
        print("Success code: " + str(code))
        cv2.imwrite("frame.jpg", image)

    #Can't Connect to WebCam
    if cap is None or not cap.isOpened():
        print 'Warning: unable to open video source: (Need Fallback function)', source
    return cap'''

if __name__ == "__main__":
    create_capture(0)
