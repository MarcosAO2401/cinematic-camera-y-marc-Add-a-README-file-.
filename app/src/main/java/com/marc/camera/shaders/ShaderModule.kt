package com.marc.camera.shaders
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
