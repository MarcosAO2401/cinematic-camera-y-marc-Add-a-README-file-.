package com.marc.camera.shaders
import android.content.Context
import android.opengl.GLES30
object ShaderModule {
fun loadShader(type: Int, source: String): Int {
val shader = GLES30.glCreateShader(type)
GLES30.glShaderSource(shader, source)
GLES30.glCompileShader(shader)
