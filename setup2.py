import os
f={
"app/src/main/AndroidManifest.xml":"<manifest xmlns:android='http://schemas.android.com/apk/res/android' package='com.marc.camera'>\n<uses-permission android:name='android.permission.CAMERA'/>\n<uses-permission android:name='android.permission.RECORD_AUDIO'/>\n<application android:label='CineCamera' android:theme='@style/Theme.AppCompat.NoActionBar'>\n<activity android:name='.MainActivity' android:exported='true'>\n<intent-filter><action android:name='android.intent.action.MAIN'/><category android:name='android.intent.category.LAUNCHER'/></intent-filter>\n</activity>\n</application>\n</manifest>",
"app/src/main/java/com/marc/camera/MainActivity.kt":"package com.marc.camera\nimport androidx.appcompat.app.AppCompatActivity\nimport android.os.Bundle\nclass MainActivity:AppCompatActivity(){\noverride fun onCreate(s:Bundle?){\nsuper.onCreate(s)\nsetContentView(R.layout.activity_main)}}",
"app/src/main/java/com/marc/camera/camera/CameraModule.kt":"package com.marc.camera.camera\nobject CameraModule",
"app/src/main/java/com/marc/camera/shaders/ShaderModule.kt":"package com.marc.camera.shaders\nobject ShaderModule",
"app/src/main/java/com/marc/camera/ai/TFLiteModule.kt":"package com.marc.camera.ai\nobject TFLiteModule",
"app/src/main/java/com/marc/camera/ai/MediaPipeModule.kt":"package com.marc.camera.ai\nobject MediaPipeModule",
"app/src/main/java/com/marc/camera/recording/HEVCModule.kt":"package com.marc.camera.recording\nobject HEVCModule",
"app/src/main/java/com/marc/camera/recording/FallbackModule.kt":"package com.marc.camera.recording\nobject FallbackModule",
"app/src/main/res/layout/activity_main.xml":"<?xml version='1.0' encoding='utf-8'?>\n<FrameLayout xmlns:android='http://schemas.android.com/apk/res/android' android:layout_width='match_parent' android:layout_height='match_parent'>\n<androidx.camera.view.PreviewView android:id='@+id/viewFinder' android:layout_width='match_parent' android:layout_height='match_parent'/>\n</FrameLayout>",
"app/src/main/res/raw/cyberpunk.glsl":"precision mediump float;\nuniform sampler2D uTexture;\nvarying vec2 vTexCoord;\nvoid main(){\nvec4 c=texture2D(uTexture,vTexCoord);\ngl_FragColor=vec4(c.r*0.5,c.g*0.8,c.b*1.5,1.0);}",
"app/src/main/res/values/strings.xml":"<resources>\n<string name='app_name'>CineCamera</string>\n</resources>",
"app/build.gradle":"plugins{id 'com.android.application'\nid 'kotlin-android'}\nandroid{compileSdk 34\ndefaultConfig{applicationId 'com.marc.camera'\nminSdk 26\ntargetSdk 34\nversionCode 1\nversionName '1.0'}}\ndependencies{\nimplementation 'androidx.camera:camera-core:1.3.0'\nimplementation 'androidx.camera:camera-camera2:1.3.0'\nimplementation 'androidx.camera:camera-lifecycle:1.3.0'\nimplementation 'androidx.camera:camera-view:1.3.0'\nimplementation 'org.tensorflow:tensorflow-lite:2.13.0'\nimplementation 'androidx.appcompat:appcompat:1.6.1'}",
"settings.gradle":"rootProject.name='CineCamera'\ninclude ':app'",
"build.gradle":"buildscript{repositories{google()\nmavenCentral()}\ndependencies{classpath 'com.android.tools.build:gradle:8.1.0'\nclasspath 'org.jetbrains.kotlin:kotlin-gradle-plugin:1.9.0'}}\nallprojects{repositories{google()\nmavenCentral()}}"
}
for p,c in f.items():
    d=os.path.dirname(p)
        if d:os.makedirs(d,exist_ok=True)
            open(p,"w").write(c)
                print("OK:"+p)