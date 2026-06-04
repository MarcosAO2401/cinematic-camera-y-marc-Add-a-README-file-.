package com.marc.camera

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
                                                            else ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.CAMERA, Manifest.permission.RECORD_AUDIO), PERMISSION_CODE)
                }

                    private fun startCamera() {
                                val cameraProviderFuture = ProcessCameraProvider.getInstance(this)
                                        cameraProviderFuture.addListener({
                                                        val cameraProvider = cameraProviderFuture.get()
                                                                    val preview = Preview.Builder().build().also { it.setSurfaceProvider(viewFinder.surfaceProvider) }
                                                                                val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA
                                                                                            try {
                                                                                                                cameraProvider.unbindAll()
                                                                                                                                cameraProvider.bindToLifecycle(this, cameraSelector, preview)
                                                                                            } catch (e: Exception) {
                                                                                                                Toast.makeText(this, "Error: ${e.message}", Toast.LENGTH_SHORT).show()
                                                                                            }
                                        }, ContextCompat.getMainExecutor(this))
                    }

                        private fun allPermissionsGranted() = arrayOf(Manifest.permission.CAMERA).all {
                                    ContextCompat.checkSelfPermission(baseContext, it) == PackageManager.PERMISSION_GRANTED
                        }

                            override fun onRequestPermissionsResult(code: Int, perms: Array<String>, results: IntArray) {
                                        super.onRequestPermissionsResult(code, perms, results)
                                                if (code == PERMISSION_CODE && allPermissionsGranted()) startCamera()
                                                        else Toast.makeText(this, "Permiso de cámara requerido", Toast.LENGTH_SHORT).show()
                            }
}git add . && git commit -m "Add MainActivity CameraX" &&    
                            }
                        }
                                                                                            }
                                                                                            }
                                        })
                    }
                }
}