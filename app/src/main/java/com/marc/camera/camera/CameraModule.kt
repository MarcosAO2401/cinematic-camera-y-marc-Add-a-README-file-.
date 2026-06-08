package com.marc.camera.camera
import androidx.camera.core.*
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.lifecycle.LifecycleOwner
object CameraModule {
fun bind(provider: ProcessCameraProvider, owner: LifecycleOwner, preview: Preview) {
provider.unbindAll()
provider.bindToLifecycle(owner, CameraSelector.DEFAULT_BACK_CAMERA, preview)
}
}
