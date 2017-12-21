import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PoolsListComponent } from './pools-list.component';

describe('PoolsListComponent', () => {
  let component: PoolsListComponent;
  let fixture: ComponentFixture<PoolsListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PoolsListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PoolsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
