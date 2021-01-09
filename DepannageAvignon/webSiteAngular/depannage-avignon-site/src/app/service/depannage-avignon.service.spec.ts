import { TestBed } from '@angular/core/testing';

import { DepannageAvignonService } from './depannage-avignon.service';

describe('DepannageAvignonService', () => {
  let service: DepannageAvignonService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DepannageAvignonService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
