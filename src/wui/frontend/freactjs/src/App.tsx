import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [sfe, setSFE] = useState<string[]>([]);
  const [eff, setEFF] = useState<string[]>([]);
  const [file, setFile] = useState<File | null>(null);
  const [seff, setSEFF] = useState<string | null>(null);
  const [status, setStatus] = useState("initial");

  useEffect(() => {
    fetchMetadata();
  }, []);

  const handleEFFChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSEFF(null);
    if (eff.includes(e.target.value)) {
      setSEFF(e.target.value);
    }
  };
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFile(null);
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const fetchMetadata = async () => {
    try {
      const result = await fetch(
        "http://0.0.0.0:8000/audio/convert",
        {
          method: "GET",
        }
      );
      if (result.status !== 200) {
        setStatus("fail>" + (await result.json())["detail"])
        return;
      }
      const data = await result.json()
      setSFE(data["SUPPORTED_FILE_EXTENSIONS"].map((item: string) => item.toUpperCase()));
      setEFF(data["SUPPORTED_EXPORT_FILE_FORMATS"].map((item: string) => item.toUpperCase()));
    } catch (error) {
      setStatus("fail>" + "Network Error");
    }
  }

  const submitFile = async () => {
    setStatus("initial");

    if (!seff) {
      setStatus("fail>`Export File Format` is not selected");
      return;
    }
    if (!file) {
      setStatus("fail>`File` is not selected");
      return;
    }
    try {
      const formData = new FormData();
      formData.append("file", file);

      const result = await fetch(
        "http://0.0.0.0:8000/audio/convert?export_file_format=" + seff.toLowerCase(),
        {
          method: "POST",
          body: formData,
        }
      );

      if (result.status !== 200) {
        setStatus("fail>" + (await result.json())["detail"])
        return;
      }
      const content_disposition: string | null= result.headers.get("Content-Disposition");
      if (!content_disposition) {
        setStatus("fail>Missing header: Content-Disposition");
        return;
      }
      const blob: Blob = await result.blob();
      const objectUrl = URL.createObjectURL(blob);
      const link: HTMLAnchorElement = document.createElement('a');

      link.href = objectUrl;
      // filename="{filename}.{export_file_format}"
      link.download = content_disposition.split("=\"")[1].slice(0, -1);
      link.click();
      URL.revokeObjectURL(objectUrl);
    } catch (error) {
      setStatus("fail>" + "Network Error");
    }
  }
  return (
    <>
      <div className="flex items-center justify-center w-full">
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <h2>+</h2>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1 className="text-2xl font-bold">Audio File Converter</h1>
      <div className="flex items-center justify-center w-full">
        <select onChange={handleEFFChange} id="countries" className="m-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
          <option defaultValue={"US"}>Select Export File Format</option>
          {eff.map((file_format) =>
           <option key={file_format} value={file_format}>{file_format}</option>
          )}
        </select>
      </div>
      <Result status={status} />
      <div className="flex items-center justify-center w-full">
        <label htmlFor="dropzone-file" className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
            <div className="flex flex-col items-center justify-center pt-5 pb-6">
                <svg className="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                  <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                </svg>
                <p className="mb-2 text-sm text-gray-500 dark:text-gray-400"><span className="font-semibold">Click to upload</span> or drag and drop</p>
                <p className="text-xs text-gray-500 dark:text-gray-400">Supported input files: {sfe}</p>
            </div>
            <input id="dropzone-file" type="file" className="hidden" onChange={handleFileChange} />
        </label>
      </div>
      <button onClick={submitFile} type="button" className="m-2 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Convert</button>
    </>
  )
}

const Result = ({ status }: { status: string }) => {
  const [flag, message] = status.split(">");
  if (flag === 'fail') {
    return <p className="mb-2">❌ {message}</p>;
  } else {
    return null;
  }
};


export default App
