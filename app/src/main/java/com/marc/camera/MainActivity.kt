import os

files = {
    "app/src/main/java/com/marc/camera/MainActivity.kt": """package com.marc.camera
    import android.Manifest
    import android.content.pm.PackageManager
    import android.os.Bundle
    import android.widget.Toast
    import androidx.appcompat.app.AppCompatActivity
    import androidx.camera.core.*
    import androidx.camera.lifecycle.ProcessCameraProvider
    import androidx.camera.view.PreviewView
    import androidx.core.app.ActivityCompat
    import androidx.core.content.ContextCompat
    class MainActivity : AppCompatActivity() {
            private lateinit var viewFinder: PreviewView
                private val PERMISSION_CODE = 10
                    override fun onCreate(savedInstanceState: Bundle?) {
                                super.onCreate(savedInstanceState)
                                        setContentView(R.layout.activity_main)
                                                viewFinder = findViewById(R.id.viewFinder)
                                                        if (allPermissionsGranted()) startCamera()
                                                                else ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.CAMERA), PERMISSION_CODE)
                    }
                        private fun startCamera() {
                                    val future = ProcessCameraProvider.getInstance(this)
                                            future.addListener({
                                                            val provider = future.get()
                                                                        val preview = Preview.Builder().build().also { it.setSurfaceProvider(viewFinder.surfaceProvider) }
                                                                                    try {
                                                                                                        provider.unbindAll()
                                                                                                                        provider.bindToLifecycle(this, CameraSelector.DEFAULT_BACK_CAMERA, preview)
                                                                                    } catch (e: Exception) {
                                                                                                        Toast.makeText(this, "Error: ${e.message}", Toast.LENGTH_SHORT).show()
                                                                                    }
                                            }, ContextCompat.getMainExecutor(this))
                        }
                            private fun allPermissionsGranted() = ContextCompat.checkSelfPermission(baseContext, Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED
                                override fun onRequestPermissionsResult(code: Int, perms: Array<String>, results: IntArray) {
                                            super.onRequestPermissionsResult(code, perms, results)
                                                    if (code == PERMISSION_CODE && allPermissionsGranted()) startCamera()
                                                            else Toast.makeText(this, "Permiso requerido", Toast.LENGTH_SHORT).show()
                                }
    }""",
    "app/src/main/java/com/marc/camera/camera/CameraModule.kt": """package com.marc.camera.camera
    import androidx.camera.core.*
    import androidx.camera.lifecycle.ProcessCameraProvider
    import androidx.lifecycle.LifecycleOwner
    object CameraModule {
            fun bind(provider: ProcessCameraProvider, owner: LifecycleOwner, preview: Preview) {
                        provider.unbindAll()
                                provider.bindToLifecycle(owner, CameraSelector.DEFAULT_BACK_CAMERA, preview)
            }
    }""",
    "app/src/main/java/com/marc/camera/shaders/ShaderModule.kt": """package com.marc.camera.shaders
    import android.content.Context
    import android.opengl.GLES20
    object ShaderModule {
            fun loadShader(type: Int, code: String): Int {
                        val shader = GLES20.glCreateShader(type)
                                GLES20.glShaderSource(shader, code)
                                        GLES20.glCompileShader(shader)
                                                return shader
            }
                fun readGLSL(ctx: Context): String {
                            return ctx.resources.openRawResource(R.raw.cyberpunk).bufferedReader().readText()
                }
    }""",
    "app/src/main/java/com/marc/camera/ai/TFLiteModule.kt": """package com.marc.camera.ai
    import android.content.Context
    object TFLiteModule {
            private var loaded = false
                fun load(ctx: Context) {
                            try {
                                            ctx.assets.openFd("model.tflite")
                                                        loaded = true
                            } catch (e: Exception) {
                                            loaded = false
                            }
                }
                    fun isLoaded() = loaded
    }""",
    "app/src/main/java/com/marc/camera/ai/MediaPipeModule.kt": """package com.marc.camera.ai
    object MediaPipeModule {
            fun isAvailable() = true
    }""",
    "app/src/main/java/com/marc/camera/recording/HEVCModule.kt": """package com.marc.camera.recording
    import android.content.Context
    import androidx.camera.video.*
    object HEVCModule {
            fun buildRecorder(): VideoCapture<Recorder> {
                        val recorder = Recorder.Builder()
                                    .setQualitySelector(QualitySelector.from(Quality.HD))
                                                .build()
                                                        return VideoCapture.withOutput(recorder)
            }
    }""",
    "app/src/main/java/com/marc/camera/recording/FallbackModule.kt": """package com.marc.camera.recording
    object FallbackModule {
            fun isHevcSupported(): Boolean {
                        return android.media.MediaCodecList(android.media.MediaCodecList.ALL_CODECS)
                                    .codecInfos.any { it.name.contains("hevc", ignoreCase = true) }
            }
    }"""
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w").write(content)
            print("OK: " + path)
            
            }
    }
            }
    }
    }
                            }
                            }
                }
    }
                }
            }
    }
            }
    }
                                }
                                                                                    }
                                                                                    }
                                            })
                        }
                    }
    }
}