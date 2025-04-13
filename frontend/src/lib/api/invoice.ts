


export async function uploadImage(image: File) {
    const formData = new FormData()
    formData.append('image', image)
  
    console.log(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/invoice`);
    const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/invoice`, {
      method: 'POST',
      body: formData,
    })
  
    if (!res.ok) throw new Error('Upload failed')
    return res.json()
  }