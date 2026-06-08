package com.marc.camera.ai
import android.content.Context
import android.graphics.Bitmap
object TFLiteModule {
private var interpreter: Any? = null
fun load(ctx: Context) {
try {
val assetFD = ctx.assets.openFd("model.tflite")
interpreter = assetFD
} catch(e: Exception) { e.printStackTrace() }
}
fun isLoaded() = interpreter != null
}
