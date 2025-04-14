"use client";
import { uploadImage } from "@/lib/api/invoice";
import React, { useState, useRef } from 'react';
import BottomDialog from '@/components/BottomDialog';

export default function Home() {
  const cameraInputRef = useRef<HTMLInputElement | null>(null);
  const galleryInputRef = useRef<HTMLInputElement | null>(null);

  const [image, setImage] = useState<string | null>(null)
  const [showDialog, setShowDialog] = useState(false);


  const handleChooiseChange = (chooise: string) => {
    if (chooise === 'gallery') {
      galleryInputRef.current?.click()
    } else if (chooise === 'camera') {
      cameraInputRef.current?.click()
    }
  }

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e?.target?.files?.[0]
    if (file) {
      const imageUrl = URL.createObjectURL(file)
      setImage(imageUrl)
      uploadImage(file).then(data => {
        console.log(data);
      }).catch(err => {
        console.log(err);
      })

    }
  }



  return (
    <main className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-6">
      <h1 className="text-2xl font-bold mb-6">Select an image</h1>

      <button
        className="px-4 py-2 bg-blue-600 text-white rounded"
        onClick={() => setShowDialog(true)}>
          Upload ticket
      </button>

      <input
          type="file"
          accept="image/*"
          ref={galleryInputRef}
          className="hidden"
          onChange={handleImageChange}
      />

      <input
          type="file"
          accept="image/*"
          ref={cameraInputRef}
          className="hidden"
          capture="environment"
          onChange={handleImageChange}
      />    

      {image && (
        <div className="mt-6">
          <p className="mb-2 text-center">Preview:</p>
          <img
            src={image}
            alt="Captured or Selected"
            className="max-w-xs rounded-lg border border-gray-600 shadow-lg"
          />
        </div>
      )}


      {showDialog && (
        <BottomDialog onClose={() => setShowDialog(false)} setChooise={handleChooiseChange} />
      )}
    </main>
  );
}
