package com.marc.camera.camera
object CameraModule {
    var isRunning = false
    fun start() { isRunning = true }
    fun stop() { isRunning = false }
}
