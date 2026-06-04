b=open('build.gradle','w')
b.write('buildscript {\n    repositories { google()\n        mavenCentral() }\n    dependencies {\n        classpath "com.android.tools.build:gradle:8.1.0"\n        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:1.9.0"\n    }\n}\nallprojects { repositories { google()\n    mavenCentral() } }\n')
b.close()
a=open('app/build.gradle','w')
a.write('plugins {\n    id "com.android.application"\n    id "kotlin-android"\n}\nandroid {\n    compileSdk 34\n    compileOptions {\n        sourceCompatibility JavaVersion.VERSION_17\n        targetCompatibility JavaVersion.VERSION_17\n    }\n    kotlinOptions { jvmTarget = "17" }\n    defaultConfig {\n        applicationId "com.marc.camera"\n        minSdk 26\n        targetSdk 34\n        versionCode 1\n        versionName "1.0"\n    }\n}\ndependencies {\n    implementation "androidx.appcompat:appcompat:1.6.1"\n    implementation "androidx.camera:camera-core:1.3.0"\n    implementation "androidx.camera:camera-camera2:1.3.0"\n    implementation "androidx.camera:camera-lifecycle:1.3.0"\n    implementation "androidx.camera:camera-view:1.3.0"\n    implementation "androidx.camera:camera-video:1.3.0"\n}\n')
a.close()
print("OK")
  