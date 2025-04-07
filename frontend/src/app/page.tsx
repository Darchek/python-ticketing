"use client";
import Camera from "@/components/Camera";
import Image from "next/image";
import React, { useState, useEffect } from 'react';


export default function Home() {

  const [data, setData] = useState('');

  useEffect(() => {

    const fetchData = async () => {

      try {
        const response = await fetch("http://localhost:5000/health");

        if (!response.ok) {
          setData(`HTTP error! Status: ${response.status}`);
          return;
        }

        const result = await response.text();
        setData(result);

      } catch (err: unknown) {
        const error = err as Error;
        console.error("Error fetching data:", error);
        setData("Error fetching data");
      }
    };

    fetchData();

  }, []);



  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-2 pb-10 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <Image
          className="dark:invert"
          src="/next.svg"
          alt="Next.js logo"
          width={180}
          height={38}
          priority
        />
        <ol className="list-inside list-decimal text-sm/6 text-center sm:text-left font-[family-name:var(--font-geist-mono)]">
          <li className="mb-2 tracking-[-.01em]">
            {data}
          </li>
        </ol>
      </main>
      <footer className="row-start-3 flex gap-[24px] flex-wrap items-center justify-center">
        <Camera />
      </footer>
    </div>
  );
}
