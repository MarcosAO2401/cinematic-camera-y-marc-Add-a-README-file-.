import os

def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(content)
    print(f'OK: {path}')

base = 'app/src/main/java/com/marc/camera'
res = 'app/src/main/res'

w(f'{base}/MainActivity.kt', '''package com.marc.camera
import android.Manifest
import android.content.pm.PackageManager
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.camera.core.CameraSelector
import androidx.camera.core.Preview
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.camera.view.PreviewView
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat

class MainActivity : AppCompatActivity() {
    private lateinit var previewView: PreviewView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        previewView = findViewById(R.id.previewView)
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED) {
            startCamera()
        } else {
            ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.CAMERA), 10)
        }
    }
    private fun startCamera() {
        val future = ProcessCameraProvider.getInstance(this)
        future.addListener({
            val provider = future.get()
            val preview = Preview.Builder().build().also {
                it.setSurfaceProvider(previewView.surfaceProvider)
            }
            provider.unbindAll()
            provider.bindToLifecycle(this, CameraSelector.DEFAULT_BACK_CAMERA, preview)
        }, ContextCompat.getMainExecutor(this))
    }
    override fun onRequestPermissionsResult(code: Int, perms: Array<String>, results: IntArray) {
        super.onRequestPermissionsResult(code, perms, results)
        if (code == 10 && results.isNotEmpty() && results[0] == PackageManager.PERMISSION_GRANTED) startCamera()
    }
}
''')

w(f'{res}/layout/activity_main.xml', '''<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <androidx.camera.view.PreviewView
        android:id="@+id/previewView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>
</FrameLayout>
''')

w(f'{base}/shaders/ShaderModule.kt', '''package com.marc.camera.shaders
import android.content.Context
import android.opengl.GLES30
object ShaderModule {
    fun loadShader(type: Int, source: String): Int {
        val shader = GLES30.glCreateShader(type)
        GLES30.glShaderSource(shader, source)
        GLES30.glCompileShader(shader)
        return shader
    }
    fun createProgram(vertSrc: String, fragSrc: String): Int {
        val vert = loadShader(GLES30.GL_VERTEX_SHADER, vertSrc)
        val frag = loadShader(GLES30.GL_FRAGMENT_SHADER, fragSrc)
        val program = GLES30.glCreateProgram()
        GLES30.glAttachShader(program, vert)
        GLES30.glAttachShader(program, frag)
        GLES30.glLinkProgram(program)
        return program
    }
    fun loadFromAssets(context: Context, filename: String): String =
        context.assets.open(filename).bufferedReader().readText()
}
''')

w(f'{base}/camera/CameraModule.kt', '''package com.marc.camera.camera
object CameraModule {
    var isRunning = false
    fun start() { isRunning = true }
    fun stop() { isRunning = false }
}
''')

w(f'{base}/ai/TFLiteModule.kt', '''package com.marc.camera.ai
object TFLiteModule {
    fun init() {}
    fun run(input: FloatArray): FloatArray = FloatArray(0)
}
''')

w(f'{base}/ai/MediaPipeModule.kt', '''package com.marc.camera.ai
object MediaPipeModule {
    fun init() {}
    fun detect(data: ByteArray): FloatArray = FloatArray(0)
}
''')

w(f'{base}/recording/HEVCModule.kt', '''package com.marc.camera.recording
object HEVCModule {
    fun record() {}
    fun stop() {}
}
''')

w(f'{base}/recording/FallbackModule.kt', '''package com.marc.camera.recording
object FallbackModule {
    fun record() {}
    fun stop() {}
}
''')

print("ALL DONE!")
