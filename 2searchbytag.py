import json

class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        if not self.query or not self._data:
            raise StopIteration
        
        try:
            self._data['items']
        except KeyError:
            raise StopIteration
    
        for item in self._data['items']:
            if not item:
                raise StopIteration
            
            thing = item.get('tags', None)
            
            if not thing:
                continue
            
            if self.query in thing:
                yield item
    

    def first(self):
        return self.search().__next__()
    


def main():
    answer=SearchByTag('movies_no_tags.json','crime')
    output=answer.search()
    try:
        for i in output:
            print(i)
    except StopIteration as e:
        print("error")
    
    #print(answer.first())

if __name__=="__main__":
    main()