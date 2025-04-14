"use client";

import { useParams } from 'next/navigation';

export default function BlogPost() {
  const params = useParams();
  return <h1>Blog Post ID: {params.id}</h1>;
}