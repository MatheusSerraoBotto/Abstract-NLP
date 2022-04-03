import * as fs from "fs";
import * as path from "path";
import { parse } from 'csv-parse';
import { abstractUtils } from "../abstracts/abstracts.utils";

type Abstract = {
  id: string;
  title: string;
  abstract: string;
};

export function read_csv(csvFilePath: string) {

  const headers = ['id', 'title', 'abstract'];
  const fileContent = fs.readFileSync(`/app/Mongo/themes/${csvFilePath}`, { encoding: 'utf-8' });

  parse(fileContent, {
    delimiter: ',',
    columns: headers,
  }, (error, result: Abstract[]) => {
    if (error) {
      console.error(error);
    }
    const theme = csvFilePath.split('.')[0].replace('_', ' ')
    result.forEach(abstract => {
      let abstract_obj = { ...abstract, theme }
      console.log(abstract_obj);

      abstractUtils.saveAbstract(abstract_obj)
    });
  })
};
