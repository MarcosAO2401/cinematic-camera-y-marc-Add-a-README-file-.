import os
files = {
'app/src/main/java/com/marc/camera/ai/MediaPipeModule.kt': 'package com.marc.camera.ai\nobject MediaPipeModule {\n    fun init() {}\n    fun detect(data: ByteArray): FloatArray = FloatArray(0)\n}\n',
'app/src/main/java/com/marc/camera/ai/TFLiteModule.kt': 'package com.marc.camera.ai\nobject TFLiteModule {\n    fun init() {}\n    fun run(input: FloatArray): FloatArray = FloatArray(0)\n}\n',
'app/src/main/java/com/marc/camera/camera/CameraModule.kt': 'package com.marc.camera.camera\nobject CameraModule {\n    fun start() {}\n    fun stop() {}\n}\n',
'app/src/main/java/com/marc/camera/recording/FallbackModule.kt': 'package com.marc.camera.recording\nobject FallbackModule {\n    fun record() {}\n    fun stop() {}\n}\n',
'app/src/main/java/com/marc/camera/recording/HEVCModule.kt': 'package com.marc.camera.recording\nobject HEVCModule {\n    fun record() {}\n    fun stop() {}\n}\n',
}
for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(content)
    print(f'Done: {path}')
