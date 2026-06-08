package com.marc.camera.recording
import android.content.Context
import androidx.camera.video.*
import androidx.core.content.ContextCompat
object HEVCModule {
fun buildRecorder(ctx: Context): VideoCapture<Recorder> {
val recorder = Recorder.Builder().setQualitySelector(QualitySelector.from(Quality.HD)).build()
return VideoCapture.withOutput(recorder)
}
}
