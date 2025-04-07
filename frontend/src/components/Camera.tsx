// components/Camera.tsx
"use client";

import React, { useRef, useCallback } from "react";
import Webcam from "react-webcam";

const videoConstraints = {
  width: 1280,
  height: 720,
  facingMode: "user",
};

export default function Camera() {
  const webcamRef = useRef<Webcam>(null);

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current?.getScreenshot();
    console.log("Captured image:", imageSrc);
  }, [webcamRef]);

  return (
    <div>
      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        videoConstraints={videoConstraints}
      />
      <button onClick={capture} className="mt-2 bg-blue-500 text-white px-4 py-2 rounded">
        Capture
      </button>
    </div>
  );
}