'use client';

import Image from 'next/image';
import GalleryIcon from "../../public/gallery.svg";
import CameraIcon from "../../public/camera.svg";

export default function BottomDialog({ onClose, setChooise }: { onClose: () => void, setChooise: (chooise: string) => void }) {

  const handleChooise = (chooise: string) => {
    setChooise(chooise);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/50 flex items-end justify-center">
      <div className="bg-white w-full max-w-md p-4 rounded-t-2xl shadow-lg">
        <h2 className="text-lg font-semibold mb-4">Upload Photo</h2>

        <button
          className="w-full py-3 mb-2 bg-blue-600 text-white rounded-md"
          onClick={() => { handleChooise('gallery') }}
        >
          Select from Gallery  <Image priority src={GalleryIcon} alt="Gallery" className="inline ml-5 mb-1" />
        </button>

        <button
          className="w-full py-3 mb-2 bg-green-600 text-white rounded-md"
          onClick={() => { handleChooise('camera') }}
        >
          Take Photo <Image priority src={CameraIcon} alt="Camera" className="inline ml-5 mb-1" />
        </button>

        <button
          className="w-full py-3 text-gray-500 mt-2"
          onClick={onClose}
        >
          Cancel
        </button>
      </div>
    </div>
  );
}
